"""

XBlock for presenting the user with a text template for generating rubrics
associated with a unit.

Author : Cary Rivet

"""

import urllib, datetime, json, urllib2

from hl_text import hl_text_XBlock
from hl_utils import HLXBlockModalHelperMixin


# imports for content indexing support
import re
# from xmodule.util.misc import escape_html_characters

from xblock.core import XBlock
from xblock.fields import (
        Scope,
        Integer,
        List,
        String,
        Boolean,
        Dict,
        Reference, # reference to another xblock
        ReferenceList, # list of references to other xblocks
    )

from xblockutils.resources import ResourceLoader
loader = ResourceLoader(__name__)

# from xblock.fragment import Fragment #DEPRECIATED
from web_fragments.fragment import Fragment




# hl-text template for rubric xblock
class HL_Rubric_text_XBlock(hl_text_XBlock):

    display_name = String(
        display_name="Display Name",
        help="This name appears in the horizontal navigation at the top of the page",
        scope=Scope.settings,
        default="Rubric (Template)"
    )

    def get_help_template(self, context=None):
        context = context or {}
        return loader.render_django_template('templates/help_template.html', context)

    def get_empty_template(self, context=None):
        context = context or {}
        return loader.render_django_template('templates/rubric_text_template.html', context)

    def studio_view(self, context=None):

        context = context or {}

        fragment = super(HL_Rubric_text_XBlock, self).studio_view(context)


        # add the custom help styling to the fragment
        fragment.add_css(loader.load_unicode('static/css/rubric_help_styling.css'))
        

        return fragment

    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("HL rubric text XBlock",
             """<hl_rubric_text/>
             """),

        ]
