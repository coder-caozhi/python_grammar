"""
    @Author:Irene
    @Time:2026/5/25
    @Desc:
"""
from setuptools import setup,find_packages

#分开打包
# # 打包第一个独立包
# def package1():
#     setup(
#         name="mygraphic", # 打包后的包名称，必须唯一
#         version="0.1.0",        # 版本说明
#         packages=["mygraphic"],  # 手动指定第一个包的目录
#         python_requires=">=3.7", # python版本要求
#     )
#
#
# # 打包第二个独立包
# def package2():
#     setup(
#         name="atguigu_math",
#         version="0.1.0",
#         packages=["mymath"],  # 手动指定第二个包的目录
#         python_requires=">=3.7",
#     )
#
# if __name__ == "__main__":
#     # package1()
#     package2()

#打总包
setup(
    name="atguigu",  # 打包后的包名称，必须唯一
    version="0.1.0", # 版本号
    packages=find_packages(),  # 自动识别主包下的所有子包
    python_requires=">=3.7", # 指定python版本
)

