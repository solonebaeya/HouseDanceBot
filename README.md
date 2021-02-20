# HouseDanceBot
需求背景：

从19年11月加入Pureflow Family（北京Puresoul舞室的House团队）之后，就有想法做一个帮助自己练习基本功的东西，于是将将！本脚本诞生了！可以通过设置基本功切换的时间来练习不同基本功之间的连贯和流畅度。

说明：

1.提前安装好pyaudio、wave、tqdm、time这些需要的包（pip install XXX），当然你把代码拷到pycharm也会提示你安装相关包。

2.其中time.asleep()设置基本功切换时间，根据个人经验，house基本功15s一切换是比较有训练效果的。

3.准备好要练习的街舞元素音频放在文件夹里，本项目文件夹'**BasicSteps/**'里的基本功音频是我自己录的，你也可以替换成别的内容，比如popping或者bk的基本功；另外的AdvancedSteps文件夹是进阶的基本功。

4.文件HouseFundationIndex是音频文件和foundation元素名的映射，方便你对音频增删改查，全部基本功的参考视频：https://www.youtube.com/watch?v=eHzyK-2HVpM。

最后，享受街舞带来的快乐，keep on dancing!(我设置的while(1),你不坚持也不行啊哈哈哈哈)
