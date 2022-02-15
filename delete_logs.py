import os, shutil

folder = ['logs/conversation', 'logs/dialogue model', 'logs/emotion classification', 'logs/event chain', 'logs/information extraction','logs/wellbeing', 'logs/user world', 'logs/vhope']

for names in folder:
    for filename in os.listdir(names):
        file_path = os.path.join(names, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print('%s successfully deleted.' %filename)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))