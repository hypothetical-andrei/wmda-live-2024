from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service 
from selenium.webdriver.firefox.options import Options 

def main():
  service = Service(executable_path='./geckodriver')
  options = Options()
  options.add_argument('--width=800')
  options.add_argument('--height=600')
  driver = webdriver.Firefox(service = service, options = options)
  driver.get('http://andrei.ase.ro')
  with open('script.js') as f:
    script = f.read()
  result = driver.execute_script(script)
  print(result)
  driver.quit()

if __name__ == '__main__':
  main()