# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/7 14:08'
# file : 'Meta.py'
# Summary : ''


import re


class DIMapper:
    __mapper_dict = {}

    @staticmethod
    def inject(cls, arg):
        if cls not in DIMapper.__mapper_dict:
            DIMapper.__mapper_dict[cls] = arg

    @staticmethod
    def get_mappers():
        return DIMapper.__mapper_dict


class DIMetaClass(type):

    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)

        mapper_dict = DIMapper.get_mappers()
        if cls in mapper_dict:
            cls.__init__(obj, mapper_dict[cls])
        else:
            cls.__init__(obj, *args, **kwargs)
        return obj


class DIMapperList:
    __mapper_dict = {}

    @staticmethod
    def inject(cls, *args):
        if cls not in DIMapperList.__mapper_dict:
            DIMapperList.__mapper_dict[cls] = list(args)

    @staticmethod
    def get_mappers():
        return DIMapperList.__mapper_dict


class DIMetaClassList(type):

    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)

        mapper_dict = DIMapperList.get_mappers()
        if cls in mapper_dict:
            group = re.compile(r'.(\w+) object')
            mapper_list = group.findall(mapper_dict[cls].__str__())
            mapper = {}
            for i in range(len(mapper_list)):
                mapper[mapper_list[i][0].lower() + mapper_list[i][1:]] = mapper_dict[cls][i]
            cls.__init__(obj, **mapper)
        else:
            cls.__init__(obj, *args, **kwargs)
        return obj

# class UserBusinessCardService(metaclass=DIMetaClassList):
#
#     def __init__(self, **kwargs):
#         # 首字母需小写
#         self.businessCardRepository = kwargs.get('businessCardRepository')
#         self.adminRepository = kwargs.get('adminRepository')
#
#     def sam(self):
#         self.businessCardRepository.sam_1()
#         self.adminRepository.sam_2()
#
#
# class BusinessCardRepository():
#
#     def sam_1(self):
#         print('sam_1')
#
#
# class AdminRepository():
#
#     def sam_2(self):
#         print('sam_2')
#
#
# def main():
#     DIMapperList.inject(UserBusinessCardService, BusinessCardRepository(), AdminRepository())
#     get_mappers = DIMapperList.get_mappers()
#     print(get_mappers)
#     userBusinessCardService = UserBusinessCardService()
#     userBusinessCardService.sam()
#     print(333)
#
#
# if __name__ == '__main__':
#     main()
