import webview
import importlib

# 加载模块
def load_module(module_name):
    return importlib.import_module(module_name)

# 重新加载模块
def reload_module(module):
    return importlib.reload(module)

# Webview 加载页面时的回调函数
def on_load():
    # 第一次加载页面时，加载模块
    global example_module
    example_module = load_module("example_module")
    webview.evaluate_js('document.getElementById("output").innerText = "第一次导入模块..."')

# 重新加载模块的回调函数
def reload():
    # 模块内容发生变化，重新加载模块
    example_module = reload_module(example_module)
    output_text = example_module.say_hello()
    webview.evaluate_js('document.getElementById("output").innerText = "{}"'.format(output_text))

if __name__ == "__main__":
    # 创建 Webview 窗口并加载 HTML 页面
    webview.create_window("Webview Example", html="<html><body><h1>Hello Webview!</h1><button onclick='reload()'>Reload Module</button><div id='output'></div><script>function reload() { webview.api.reload(); }</script></body></html>", js_api=reload)
    # 注册 Webview 的加载事件回调函数
    webview.start(on_load)
