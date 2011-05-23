def organize_groupr(module):
    card_list = module.get('card_list')
    organize_card_list(card_list, module)
    return module

def organize_card_list(card_list, module):
    for card in card_list:
        card = organize_card(card, module)
    return card_list

def organize_card(card, module):
    function_map = {
        'card_1' : organize_card_1,
        'card_2' : organize_card_2,
        'card_3' : organize_card_3,
        'card_4' : organize_card_4,
        'card_5' : organize_card_5,
        'card_6a' : organize_card_6a,
        'card_6b' : organize_card_6b,
        'card_7a' : organize_card_7a,
        'card_7b' : organize_card_7b,
        'card_8a' : organize_card_8a,
        'card_8b' : organize_card_8b,
        'card_8c' : organize_card_8c,
        'card_8d' : organize_card_8d,
        'card_9' : organize_card_9,
        'card_10' : organize_card_10,
    }
    card_name = card.get('card_name')
    card_function = function_map.get(card_name, card_dummy)
    try:
        card = card_function(card, module)
    except OrganizeError:
        pass
    except SemanticError:
        pass
    return card

def card_dummy(card):
    return card

def organize_card_1(card, module):
    pass

def organize_card_2(card, module):
    pass

def organize_card_3(card, module):
    pass

def organize_card_4(card, module):
    pass

def organize_card_5(card, module):
    pass

def organize_card_6a(card, module):
    pass

def organize_card_6b(card, module):
    pass

def organize_card_7a(card, module):
    pass

def organize_card_7b(card, module):
    pass

def organize_card_8a(card, module):
    pass

def organize_card_8b(card, module):
    pass

def organize_card_8c(card, module):
    pass

def organize_card_8d(card, module):
    pass

def organize_card_9(card, module):
    pass

def organize_card_10(card, module):
    pass
