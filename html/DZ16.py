from jinja2 import Environment, FileSystemLoader, Template

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
title = 'Домашнее задание'
h1 = 'Страница с домашним заданием.'
p = 'Домашнее задание выполненно!!!'

tm = env.get_template('main.html')
# tm = Template(html)
msg = tm.render(title=title, h1=h1, p=p)

print(msg)
