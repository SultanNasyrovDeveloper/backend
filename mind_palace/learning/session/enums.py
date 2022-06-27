from mind_palace.core.enums import DjangoChoicesEnum


class UserLearningSessionStatusEnum(DjangoChoicesEnum):

    active = 'active'
    finished = 'finished'
