import random
import webview
import yaml


class Api:
    def __init__(self, config):
        self.disable_flag = False
        self.config = config

    def getPort(self):
        response = {'message': config['port']}
        return response

    def getConfig(self):
        return {'message': config}

    def setNewValue(self, new_value):
        config['new_value'] = new_value
        with open('config.yaml', 'w') as f:
            yaml.dump(config, f)

    def getRandomNumber(self):
        response = {
            'message': 'Here is a random number courtesy of randint: {0}'.format(random.randint(0, 100000000))
        }
        return response

    def error(self):
        raise Exception('This is a Python exception')


def on_load(window, css):
    window.evaluate_js('console.log("LOG: backend thread is ready")')
    window.load_css(css)

def post_processing():
    pass


if __name__ == '__main__':
    with open('./gui/config.yaml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    with open('./gui/win-main.html', 'r') as h, open('./gui/win-main.css', 'r') as c:
        html = h.read()
        css = c.read()

    api = Api(config)
    window = webview.create_window('Main board', html=html, js_api=api)
    webview.start(on_load, (window, css), gui='cef', debug=True)

    post_processing()
