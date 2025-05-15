# Personal-knowledge-base
基于coze调用api实现个人知识库问答系统

## 效果展示
![效果展示](https://github.com/Tom-grb/Personal-knowledge-base/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-05-15%20175328.png)

## 项目简介
本项目是一个基于Coze API的个人知识库问答系统，通过Flask框架提供Web服务接口，实现智能问答功能。

## 功能说明https://github.com/Tom-grb/Personal-knowledge-base/blob/main/README.md
- 提供Web界面进行问答交互
- 调用Coze API实现智能问答

## API使用方法
1. 启动服务后，访问根路径`/`获取Web界面
2. 发送POST请求到`/message`接口进行问答，参数为`msg`

## 运行指南
1. 安装依赖: `pip install flask requests`
2. 运行服务: `python app.py`
3. 默认访问地址: `http://127.0.0.1:8808`
