python down.py
echo "down complete"
python parse.py
echo "parse complete"
python view.py
echo "view complete"
python update_db.py
echo "update_db complete"
cp info.sqlite /home/hsb/public_html
