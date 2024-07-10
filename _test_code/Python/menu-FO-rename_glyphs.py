# menuTitle : (Start-up) (FO) Rename Glyphs
# author: Ryan Bugden

import ezui
from mojo.subscriber import Subscriber, registerFontOverviewSubscriber
from mojo.UI import CurrentFontWindow


EXTENSION_KEY = 'com.ryanbugden.glyphRenamer.settings'


class GlyphRenamer(ezui.WindowController):

    def build(self, parent):
        window = parent.w
        self.f = RFont(parent._font)
        self.glyphs_to_rename = self.f.selectedGlyphNames
        
        content = """
        (X) Rename            @operationRadios
        ( ) Find / Replace
        ( ) Add to Name
        ( ) Force New Suffix
        
        ---
        
        [_ _]                 @renameTextField
        
        * HorizontalStack     @findReplaceStack
        > [_ _]               @findTextField
        > →                   @arrowLabel
        > [_ _]               @replaceTextField
        
        [_ _]                 @addToNameTextField
        
        . [_ _]                @forceSuffixTextField

        ======================
        
        (Cancel)              @cancelButton
        (Apply)               @applyButton
        """
        entry_width = 160
        button_width = (entry_width - 10) / 2
        descriptionData = dict(
            renameTextField=dict(
                valueWidth=entry_width,
            ),
            findReplaceStack=dict(
                width=entry_width,
            ),
            findTextField=dict(
                width=(entry_width - 32) / 2,
            ),
            replaceTextField=dict(
                width="fill",
            ),
            cancelButton=dict(
                width=button_width,
            ),
            applyButton=dict(
                width=button_width,
            )
        )
        self.w = ezui.EZSheet(
            content=content,
            descriptionData=descriptionData,
            size="auto",
            parent=window,
            controller=self
        )
        self.operation = self.w.getItem("operationRadios")
        self.rename_field = self.w.getItem("renameTextField")
        self.find_field = self.w.getItem("findTextField")
        self.replace_field = self.w.getItem("replaceTextField")
        self.add_to_field = self.w.getItem("addToNameTextField")
        self.force_suffix_field = self.w.getItem("forceSuffixTextField")
        self.find_replace_stack = self.w.getItem("findReplaceStack")
        self.apply_button = self.w.getItem("applyButton")
        self.cancel_button = self.w.getItem("cancelButton")
        self.cancel_button.bind(chr(27), [])
        self.w.setDefaultButton(self.apply_button)
        if len(self.glyphs_to_rename) > 1:
            self.operation.set(1)
        self.update_field_options()
        
    def started(self):
        self.rename_field.set(self.glyphs_to_rename[0])
        replace = self.glyphs_to_rename[0]
        for g_name in self.glyphs_to_rename:
            if "." in g_name:
                replace = "." + g_name.split(".")[-1]
                break
        self.find_field.set(replace)
        self.replace_field.set(replace)
        self.w.open()
        
    def cancelButtonCallback(self, sender):
        self.w.close()
        
    def applyButtonCallback(self, sender):
        kwargs = dict(renameComponents=True, renameGroups=True, renameKerning=True, renameInLayers=True)
        for g_name in self.glyphs_to_rename:
            from_name, to_name = g_name, g_name
            # Rename
            if self.operation.get() == 0:
                to_name = self.rename_field.get()
            # Replace
            elif self.operation.get() == 1:
                to_name = g_name.replace(self.find_field.get(), self.replace_field.get())
            # Add to name
            elif self.operation.get() == 2:
                to_name = g_name + self.add_to_field.get()
            # Force suffix
            elif self.operation.get() == 3:
                to_name = ".".join([g_name.split(".")[0], self.force_suffix_field.get()])
            if from_name != to_name:
                self.f.renameGlyph(from_name, to_name, **kwargs)
        self.w.close()
                
    def operationRadiosCallback(self, sender):
        self.update_field_options()
        
    def update_field_options(self):
        self.rename_field.enable(True)
        if len(self.glyphs_to_rename) > 1:
            self.rename_field.enable(False)
        if self.operation.get() == 0:
            self.rename_field.show(True)
            self.find_replace_stack.show(False)
            self.add_to_field.show(False)
            self.force_suffix_field.show(False)
        elif self.operation.get() == 1:
            self.rename_field.show(False)
            self.find_replace_stack.show(True)
            self.add_to_field.show(False)
            self.force_suffix_field.show(False)
        elif self.operation.get() == 2:
            self.rename_field.show(False)
            self.find_replace_stack.show(False)
            self.add_to_field.show(True)
            self.force_suffix_field.show(False)
        elif self.operation.get() == 3:
            self.rename_field.show(False)
            self.find_replace_stack.show(False)
            self.add_to_field.show(False)
            self.force_suffix_field.show(True)

        
class RenameGlyphs(Subscriber):
    
    def fontOverviewWantsContextualMenuItems(self, info):
        self.f = CurrentFont()
        self.fo = info['fontOverview']

        if len(self.f.selectedGlyphNames) > 1:
            message = "Rename Glyphs..."
        else:
            message = "Rename Glyph..."
        my_menu_items = [
            (message, self.renameGlyphsCallback)
            ]
        info['itemDescriptions'].extend(my_menu_items)

    def renameGlyphsCallback(self, sender):
        parent = CurrentFontWindow()
        GlyphRenamer(parent)
        

if __name__ == "__main__":    
    registerFontOverviewSubscriber(RenameGlyphs)