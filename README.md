使用说明  本次api引用 https://github.com/chatanywhere/GPT_API_free

演示站 http://140.83.38.156/


后端使用python3环境安装
需要安装最新得openai库
先安装python3基础模块 和pip 然后安装下方模块环境
pip install python-telegram-bot openai
pip install openai==0.28
pip install flask![Image](https://github.com/user-attachments/assets/e721414c-da47-4f8c-9eef-b09ac43d086a)

pip install flask-cors
安装screen
screen -r -m创建新的屏幕

如果上述环境无法安装或者报错请安装虚拟环境后重新安装
安装虚拟环境
sudo apt install python3-venv
创建虚拟环境
python3 -m venv myenv
激活虚拟环境
source myenv/bin/activate

创建新的环境后使用python3 aiwy.py就可以正常运行了 修改aiwy.py内得API.KEY内容 修改为你的openai KEY
修改index.html内得后端请求IP 为你自己后端IP
