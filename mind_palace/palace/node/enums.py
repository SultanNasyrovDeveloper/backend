from mind_palace.application.enums import DjangoChoicesEnum


class NodeBodyTypeEnum(DjangoChoicesEnum):

    TEXT = 'text'
    CODE = 'code'
    CHESS = 'chess'
    TRANSLATION = 'translation'
    MICROEXPRESSION = 'microexpression'
    BIOGRAPHY = 'biography'
    HISTORICAL_EVENT = 'historical_event'