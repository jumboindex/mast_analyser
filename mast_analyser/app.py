from app.app import App

# originally I wanted to run this file as module i.e. python -m mast_analyser
# when in the top level directory

mast_analyser = App()

if __name__ == '__main__':
  mast_analyser.run()