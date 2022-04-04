def find_course(soup, course_quantity):
    course_len= soup.find('li', {'class': 'careers__list__item --programacao'}).findAll('li', class_ = 'careers__list__item__list__item')
    course_quantity.append(len(course_len))

    course_len= soup.find('li', {'class': 'careers__list__item --front-end'}).findAll('li', class_ = 'careers__list__item__list__item')
    course_quantity.append(len(course_len))

    course_len= soup.find('li', {'class': 'careers__list__item --data-science'}).findAll('li', class_ = 'careers__list__item__list__item')
    course_quantity.append(len(course_len))

    course_len= soup.find('li', {'class': 'careers__list__item --devops'}).findAll('li', class_ = 'careers__list__item__list__item')
    course_quantity.append(len(course_len))

    course_len= soup.find('li', {'class': 'careers__list__item --design-ux'}).findAll('li', class_ = 'careers__list__item__list__item')
    course_quantity.append(len(course_len))

    course_len= soup.find('li', {'class': 'careers__list__item --mobile'}).findAll('li', class_ = 'careers__list__item__list__item')
    course_quantity.append(len(course_len))

    course_len= soup.find('li', {'class': 'careers__list__item --inovacao-gestao'}).findAll('li', class_ = 'careers__list__item__list__item')
    course_quantity.append(len(course_len))
    return course_quantity