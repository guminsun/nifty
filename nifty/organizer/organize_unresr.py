from nifty.environment import helpers as env
from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
from nifty.environment.exceptions import SemanticError
import organizer_helpers as helper

##############################################################################
# Organize unresr. Put together into an orderly, functional, structured whole.

def organize_unresr(module):
    card_list = module.get('card_list')
    organize_card_list(card_list, module)
    return module

def organize_card_list(card_list, module):
    card_iter = env.get_card_iterator(module)
    organize_card_1(env.next(card_iter), module)
    # Number of card_2's denotes the number of materials to process. Each
    # card_2 is assumed to have an accompanying card_3 and card_4 which
    # defines the temperatures and sigma zero values, respectively.
    number_of_card_2 = len(env.get_cards('card_2', module))
    # The last card 2 should not be considered as a next material to process,
    # since it is expected to terminate the execution of unresr.
    # Therefore, 'number_of_card_2-1' is used to create the range to iterate
    # over.
    for c2 in range(number_of_card_2-1):
        card_2, ntemp, nsigz = organize_card_2(env.next(card_iter), module)
        # XXX: Assuming card 3 is only defined when there actually are temps
        # that should be defined.
        if ntemp > 0:
            organize_card_3(ntemp, env.next(card_iter), module)
        # XXX: Assuming card 4 is only defined when there actually are sigz
        # that should be defined.
        if nsigz > 0:
            organize_card_4(nsigz, env.next(card_iter), module)
    # The last card is expected to be a card 2 with matd = 0, to indicate
    # termination of unresr.
    organize_card_2_stop(env.next(card_iter), module)
    return module

def organize_card_1(card, module):
    # If 'card' is not card 1, then return the original card such that e.g.
    # the analyzer is able to report any semantical errors.
    if not helper.is_expected_card('card_1', card):
        return card
    expected_map = {
        0 : ('identifier', ('nendf', None)),
        1 : ('identifier', ('nin', None)),
        2 : ('identifier', ('nout', None)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_2(card, module):
    if not helper.is_expected_card('card_2', card):
        return card
    expected_map = {
        0 : ('identifier', ('matd', None)),
        1 : ('identifier', ('ntemp', None)),
        2 : ('identifier', ('nsigz', None)),
        3 : ('identifier', ('iprint', 0)),
    }
    card = helper.organize_card(expected_map, card)
    ntemp = helper.get_identifier_value('ntemp', card)
    nsigz = helper.get_identifier_value('nsigz', card)
    return card, ntemp, nsigz

def organize_card_3(ntemp, card, module):
    if not helper.is_expected_card('card_3', card):
        return card
    if ntemp is None:
        organize_error()
    expected_map = {}
    for i in range(ntemp):
        expected_map[i] = ('array', ('ntemp', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_4(nsigz, card, module):
    if not helper.is_expected_card('card_4', card):
        return card
    if nsigz is None:
        organize_error()
    expected_map = {}
    for i in range(nsigz):
        expected_map[i] = ('array', ('sigz', None, i))
    return helper.organize_card(expected_map, card)
