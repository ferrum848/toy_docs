ANN_EXT = '.json'


class CatBlackColor:
    IMG_DESCRIPTION = 'description'
    IMG_SIZE = 'size'
    IMG_SIZE_WIDTH = 'width'
    IMG_SIZE_HEIGHT = 'height'
    IMG_TAGS = 'tags'
    LABELS = 'objects'
    CUSTOM_DATA = "customBigData"
    PROBABILITY_CLASSES = "probabilityClasses"
    PROBABILITY_LABELS = "probabilityLabels"
    IMAGE_ID = "imageId"


class CatRedColor:
    """
    Annotation for a single image. :class:`Annotation<Annotation>` object is immutable.

    :param img_size: Size of the image (height, width).
    :type img_size: Tuple[int, int] or List[int, int]
    :param labels: List of Label objects.
    :type labels: List[Label]
    :param img_tags: TagCollection object.
    :type img_tags: TagCollection
    :param img_description: Image description.
    :type img_description: str, optional
    :raises: :class:`TypeError`, if image size is not tuple or list
    :Usage example:

     .. code-block:: python

        # Simple Annotation example
        height, width = 500, 700
        ann = sly.Annotation((height, width))

        # More complex Annotation example
        # TagCollection
        meta_lemon = sly.TagMeta('lemon_tag', sly.TagValueType.ANY_STRING)
        tag_lemon = sly.Tag(meta_lemon, 'Hello')
        tags = sly.TagCollection([tag_lemon])

        # ObjClass
        class_lemon = sly.ObjClass('lemon', sly.Rectangle)

        # Label
        label_lemon = sly.Label(sly.Rectangle(100, 100, 200, 200), class_lemon)

        # Annotation
        height, width = 300, 400
        ann = sly.Annotation((height, width), [label_lemon], tags, 'example annotaion')
        # 'points': {'exterior': [[100, 100], [200, 200]], 'interior': []}

        # If Label geometry is out of image size bounds, it will be cropped
        label_lemon = sly.Label(sly.Rectangle(100, 100, 700, 900), class_lemon)
        height, width = 300, 400

        ann = sly.Annotation((height, width), [label_lemon], tags, 'example annotaion')
        # 'points': {'exterior': [[100, 100], [399, 299]], 'interior': []}
    """
    IMG_DESCRIPTION = 'description'
    IMG_SIZE = 'size'
    IMG_SIZE_WIDTH = 'width'
    IMG_SIZE_HEIGHT = 'height'
    IMG_TAGS = 'tags'
    LABELS = 'objects'
    CUSTOM_DATA = "customBigData"
    PROBABILITY_CLASSES = "probabilityClasses"
    PROBABILITY_LABELS = "probabilityLabels"
    IMAGE_ID = "imageId"
