## vscode 安装python环境
先在vs里下载python，设置里边加
``` json
{
    "workbench.colorTheme": "One Dark Pro",
    "editor.formatOnPaste": true,
    "editor.formatOnSave": true,
    "workbench.editor.enablePreview": false,
    "workbench.layoutControl.enabled": false,
    "files.autoSave": "afterDelay"
}
```
</> python
print ("Hello, World!") 

###配置成功显示
PS D:\python\shixi> & C:/Users/33493/AppData/Local/Programs/Python/Python312/python.exe d:/python/shixi/.vscode/hello.py
hello world
PS D:\python\shixi> 
### 使用三种主流的包管理工具来安装 numpy：
* 先打开终端 查看pip版本
* 直接安装numpy ` pip install --user numpy `
* 进入python交互环境查看numpy
### 安装pixi环境
* 打开 PowerShell 终端(管理员身份)
* 去pixi官网复制windows的下载链接 `powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex" `
* 输入`pixi --version`看是否安装成功
* 安装完成后初始化pixi`pixi init projects `
* 进入工作区 `cd projects`
* 创建python环境可指定版本`pixi add python `
### 绘制圆
* 安装必要的包 `pixi add numpy matplotlib`
*  通过 numpy 和 matplotlib 绘制一个圆
```
 import numpy as np
import matplotlib.pyplot as plt

# 创建一个角度数组
theta = np.linspace(0, 2 * np.pi, 100)

# 使用参数方程表示圆的 x 和 y 坐标
x = np.cos(theta)
y = np.sin(theta)

# 创建图形
plt.figure(figsize=(6, 6))

# 绘制圆
plt.plot(x, y)

# 设置图形的比例，使其为圆形
plt.gca().set_aspect('equal', adjustable='box')

# 设置坐标轴的范围
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

# 添加标题
plt.title('Circle using numpy and matplotlib')

# 显示图形
plt.show() 
```
![alt text](image.png)
### qt  环境配置
* python哔哩哔哩课02


### qtwidgets Designer部件属性编译器
* placeholderText可以是输入框中填提示语
* windowTitle 设置窗口标题
* plain text edit纯文本框没有plain是富文本框

### 信号和槽signal slot
* 相当于院长和病人，院长是槽，病人是信号
* 点击信号 `button.clicked.connect(self.hello)`

### py和ui的结合，逻辑实现界面
*  ` QMessageBox.information(self, "成功", "登录成功") `登陆成功后，会弹出来一个小界面显示登陆成功，然后点击确定，跳转到主页面
* 跳转界面和调整主页面大小
`self.setWindowTitle("主界面")
        self.resize(800, 600)`
* 启动就最大化
 ` self.main = MainWindow()
self.main.showMaximized()   #👈 全屏但有边框
self.close()`
* 真正全屏（类似视频播放器）
`self.main.showFullScreen()`

### 登陆界面的思路
* 先用designer把大框架拉出来导入到vscode里边(ui会自动生成相对应的py)
* 创建main.py (分三步)
1.导入库
2.定义窗口类（主窗口和登录窗口）
3.程序入口

