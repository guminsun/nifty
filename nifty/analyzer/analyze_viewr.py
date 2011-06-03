from nifty.environment import helpers as env
import analyzer_rules as rule

from nifty.settings import viewr_settings

##############################################################################
# Analyze viewr. Checks if viewr is somewhat semantically correct.

def analyze_viewr(module):
    analyze_viewr_card_list(module)
    return module

def analyze_viewr_card_list(module):
    card_iter = env.get_card_iterator(module)
    # NJOY User Input Instructions says there are two card 1's. Treat the
    # first card as a card named 'card_0' though, just like in plotr.
    analyze_viewr_card_0(env.next(card_iter), module)
    # XXX: viewr card 1 through 14 does not have to be defined. See e.g.
    # NJOY Test Problem 06 where only card 0 (card 1 according to the NJOY
    # User Input Instructions) has been defined.
    # In order to properly analyse the semantics of viewr, the NJOY source
    # code has to be studied in greater detail.
    #
    # Pass card 1 through 14 for now.
    return module

def analyze_viewr_card_0(card, module):
    rule.card_must_be_defined('card_0', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = viewr_settings.card_0_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card
