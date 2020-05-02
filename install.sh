echo "Installing.."
echo " - libgpoid2"
sudo apt-get install -y libgpiod2
echo " - PIP sequence"
pip install -r requirements.txt
echo " - Complete, now run python monitor.py"