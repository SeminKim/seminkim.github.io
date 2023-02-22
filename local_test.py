import shutil
import os


def test_local():
    shutil.copyfile('_config.yml', '_config_local.yml')
    with open('_config_local.yml', 'a') as file:
        file.write("theme: jekyll-theme-hydejack")
    os.system('bundle exec jekyll serve --config _config_local.yml')


if __name__ == '__main__':
    try:
        test_local()
    except KeyboardInterrupt:
        if os.path.exists('_config_local.yml'):
            os.remove('_config_local.yml')
