let elements = document.querySelectorAll('li.profile')

const result = {}

for (const element of elements) {
  const role = element.querySelector('p.character')
  if (role.innerHTML.startsWith('Director')) {
    const content = element.querySelector('a')
    result['director'] = content.innerHTML
  }
}

elements = document.querySelectorAll('section.facts p')
for (const element of elements) {
  if (element.innerText.indexOf('Budget') !== -1) {
    result['budget'] = element.innerText.split('\n')[1]
  }
}

elements = document.querySelector('#reviews span')
result['review_count'] = elements.innerText

return result