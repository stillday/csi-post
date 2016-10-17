#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

    def post(self):
        # Hair color
        hair_black = "CCAGCAATCGC"
        hair_brown = "GCCAGTGCCG"
        hair_blonde = "TTAGCTATCGC"

        # Facial shape
        face_square = "GCCACGG"
        face_round = "ACCACAA"
        face_oval = "AGGCCTCA"

        # Eye color
        eye_blue = "TTGTGGTGGC"
        eye_green = "GGGAGGTGGC"
        eye_brown = "AAGTAGTGAC"

        # Gender
        gender_female = "TGAAGGACCTTC"
        gender_male = "TGCAGGAACTTC"

        # Race:
        race_white = "AAAACCTCA"
        race_black = "CGACTACAG"
        race_asian = "CGCGGGCCG"

        dna = raw_input("Please input the DNA: ")

        # Eva
        if (dna.find(gender_female) >= 0) and (dna.find(race_white) >= 0) and (dna.find(hair_blonde) >= 0) and (
            dna.find(eye_blue) >= 0) and (dna.find(face_oval) >= 0):
            print "Eva eat the Ice Cream"

        # Larissa
        if (dna.find(gender_female) >= 0) and (dna.find(race_white) >= 0) and (dna.find(hair_brown) >= 0) and (
            dna.find(eye_brown) >= 0) and (dna.find(face_oval) >= 0):
            print "Larissa eat the Ice Cream"

        # Matji
        if (dna.find(gender_male) >= 0) and (dna.find(race_white) >= 0) and (dna.find(hair_black) >= 0) and (
            dna.find(eye_blue) >= 0) and (dna.find(face_oval) >= 0):
            print "Matji eat the Ice Cream"

        # Miha
        if (dna.find(gender_male) >= 0) and (dna.find(race_white) >= 0) and (dna.find(hair_brown) >= 0) and (
            dna.find(eye_green) >= 0) and (dna.find(face_square) >= 0):
            print "Miha eat the Ice Cream"


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
