goods = []
features = {'Название':  '', 'Цена':  '', 'Количество':  '', 'Единица измерения':  ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Единица измерения': []}
num = 0
feature_ = None
control = None
while True:
    control = input(" Для продолжения нажмите: 'Enter', Для выхода нажмите: 'Q',"
                    " Для просмотра аналитики нажмите: 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\nАналитика:')
        for key, value in analytics.items():
            print(f'{key[:25]:>1}: {value}')
    for f in features.keys():
        feature_ = input(f'\nВведите характеристику: "{f}"')
        features[f] = int(feature_) if (f == 'Цена' or f == 'Количество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
