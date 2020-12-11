from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class ImageAndTextBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        help_text="A full width image with a title.",
    )
    title = blocks.CharBlock(max_length=60)

    class Meta:
        template="streams/image_and_text_block.html"
        icon = "image"
        label = "Image & Text"

class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        help_text="A full width image.",
    )

    class Meta:
        template="streams/image_block.html"
        icon = "image"
        label = "Image"

class ImageCenteredBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        help_text="A centered image.",
    )

    class Meta:
        template="streams/image_centered_block.html"
        icon = "image"
        label = "Centered Image"

class RichtextBlock(blocks.RichTextBlock):
    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full Richtext Editor"
        help_text = "A richtext editor for writing content."

class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required=True,
        help_text='Text to display',
    )

    class Meta:
        template = "streams/title_block.html"
        icon = "title"
        label = "Title"
        help_text =  "Centered Text to display on the page"

class ParagraphBlock(blocks.StructBlock):
    text = blocks.TextBlock(
        required=True,
        help_text="Paragraph to display text"
    )

    class Meta:
        template = "streams/paragraph_block.html"
        icon = "pilcrow"
        label = "Paragraph"
        help_text =  "Left aligned text to be displayed on the page."

class BlockquoteBlock(blocks.StructBlock):
    text = blocks.TextBlock(
        required=True,
        help_text="Quote to be display on the page."
    )

    attribution = blocks.CharBlock(
        max_length=100,
        help_text="Attribution",
    )

    class Meta:
        template = "streams/blockquote_block.html"
        icon = "openquote"
        label = "Blockquote"
        help_text =  "A full width quote to display on the page."