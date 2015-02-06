import sublime
import sublime_plugin

# Provide completions that match just after typing an opening angle bracket


class ExtensionsCompletions(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):
        # Only trigger within HTML
        if not view.match_selector(locations[0],
                                   "text.html - source"):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        if ch != '<':
            return []

        headers_footers = [
            ("ion-header-bar\tIonic Extension",
             'ion-header-bar align-title="${1:left}" class="${2:bar-positive}">$0</ion-header-bar>'),
            ("ion-footer-bar\tIonic Extension",
             'ion-footer-bar align-title="${1:left}" class="${2:bar-assertive}">$0</ion-footer-bar>')
        ]

        content = [
            ("ion-content\tIonic Extension",
             'ion-content has-subheader="${1:false}">$0</ion-content>'),
            ("ion-refresher\tIonic Extension",
             'ion-refresher pulling-text="${1:Pull to refresh...}" on-refresh="${2:doRefresh()}">$0</ion-refresher>'),
            ("ion-pane\tIonic Extension", 'ion-pane>$0</ion-pane>')
        ]

        lists = [
            ("ion-list\tIonic Extension", 'ion-list>$0</ion-list>'),
            ("ion-item\tIonic Extension", 'ion-item href="#">$0</ion-item>'),
            ("ion-delete-button\tIonic Extension",
             'ion-delete-button class="${1:ion-minus-circled}">$0</ion-delete-button>'),
            ("ion-reorder-button\tIonic Extension",
             'ion-reorder-button class="${1:ion-navicon}" on-reorder="${2:moveItem(item, \$fromIndex, \$toIndex)}">$0</ion-reorder-button>'),
            ("ion-option-button\tIonic Extension",
             'ion-option-button class="${1:button-positive}">$0</ion-option-button>')
        ]

        forms = [
            ("ion-checkbox\tIonic Extension",
             'ion-checkbox ng-model="${1:isChecked}">${2:Checkbox Label}</ion-checkbox>'),
            ("ion-radio\tIonic Extension",
             'ion-radio ng-model="${1:choice}" ng-value="${2:\'A\'}">${3:Choose A}</ion-radio>'),
            ("ion-toogle\tIonic Extension",
             'ion-toggle ng-model="${1:airplaneMode}" toggle-class="${2:toggle-calm}">${3:Airplane Mode}</ion-toggle>')
        ]

        tabs = [
            ("ion-tabs\tIonic Extension", 'ion-tabs class=":tabs-${1:positive} ${2:tabs-icon-only}">$0</ion-tabs>'),
            ("ion-tab\tIonic Extension", 'ion-tab title="${1:Title}" href="${2:tab-link}" icon-on="${3:icon_on}" icon-off="${4:icon_off}">$0</ion-tab>')
        ]

        modal = [
            ("ion-modal-view\tIonic Extension", 'ion-modal-view>$0</ion-modal-view>')
        ]

        navigation = [
            ("ion-nav-view\tIonic Extension", 'ion-nav-view>$0</ion-nav-view>'),
            ("ion-view\tIonic Extension", 'ion-view view-title="${1:Your Title!}">$0</ion-view>'),
            ("ion-nav-bar\tIonic Extension", 'ion-nav-bar class="${1:bar-positive}" align-title="${2:left}">$0</ion-nav-bar>'),
            ("ion-nav-buttons\tIonic Extension", 'ion-nav-buttons side="${1:primary}">$0</ion-nav-buttons>'),
            ("ion-nav-back-button\tIonic Extension", 'ion-nav-back-button class="${1:button-clear}">$0</ion-nav-back-button>'),
            ("ion-nav-title\tIonic Extension", 'ion-nav-title>$0</ion-nav-title>')
        ]

        # side_menus = [
        #     ("ion-side-menus\tIonic Extension", 'ion-side-menus>$0</ion-side-menus>'),
        #     ("ion-side-menu-content\tIonic Extension", 'ion-side-menu-content drag-content="${1:true}">$0</ion-side-menu-content>'),
        #     ("ion-side-menu\tIonic Extension", 'ion-side-menu side="${1:left}">$0</ion-side-menu>')
        # ]

        # scroll = [
        #     ("ion-scroll\tIonic Extension", 'ion-scroll>$0</ion-scroll>'),
        #     ("ion-infinite-scroll\tIonic Extension", 'ion-infinite-scroll on-infinite="${1:loadMore()}">$0</ion-infinite-scroll>')
        # ]

        # slide_box = [
        #     ("ion-slide-box\tIonic Extension", 'ion-slide-box on-slide-changed="${1:slideHasChanged($index)}">$0</ion-slide-box>'),
        #     ("ion-slide\tIonic Extension", 'ion-slide>$0</ion-slide>'),
        # ]

        # events = [
        #     ("button-on-hold\tIonic Extension", 'button on-hold="${1:onHold()}" class="${2:button}">$0</button>'),
        #     ("button-on-tap\tIonic Extension", 'button on-tap="${1:onTap()}" class="${2:button}">$0</button>'),
        #     ("button-on-touch\tIonic Extension", 'button on-touch="${1:onTouch()}" class="${2:button}">$0</button>'),
        #     ("button-on-release\tIonic Extension", 'button on-release="${1:onRelease()}" class="${2:button}">$0</button>'),
        #     ("button-on-drag\tIonic Extension", 'button on-drag="${1:onDrag()}" class="${2:button}">$0</button>'),
        #     ("button-on-drag-up\tIonic Extension", 'button on-drag-up="${1:onDragUp()}" class="${2:button}">$0</button>'),
        #     ("button-on-drag-down\tIonic Extension", 'button on-drag-down="${1:onDragDown()}" class="${2:button}">$0</button>'),
        #     ("button-on-drag-right\tIonic Extension", 'button on-drag-right="${1:onDragRight()}" class="${2:button}">$0</button>'),
        #     ("button-on-drag-left\tIonic Extension", 'button on-drag-left="${1:onDragLeft()}" class="${2:button}">$0</button>'),
        #     ("button-on-swipe\tIonic Extension", 'button on-swipe="${1:onSwipe()}" class="${2:button}">$0</button>'),
        #     ("button-on-swipe-up\tIonic Extension", 'button on-swipe-up="${1:onSwipeUp()}" class="${2:button}">$0</button>'),
        #     ("button-on-swipe-down\tIonic Extension", 'button on-swipe-down="${1:onSwipeDown()}" class="${2:button}">$0</button>'),
        #     ("button-on-swipe-left\tIonic Extension", 'button on-swipe-left="${1:onSwipeLeft()}" class="${2:button}">$0</button>'),
        #     ("button-on-swipe-right\tIonic Extension", 'button on-swipe-right="${1:onSwipeRight()}" class="${2:button}">$0</button>')
        # ]

        # completions =  tabs + side_menus + navigation + headers_footers + \
        #                 content + scroll + lists + form_inputs + \
        #                 slide_box + events

        completions = headers_footers + content + lists + forms + tabs + modal + navigation

        return (completions, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
