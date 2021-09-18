# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, redirect, url_for, request, json
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound
import include.conexion as cnx

@blueprint.route('/index')
@login_required
def index():

    return render_template('index.html', segment='index')

@blueprint.route('/listasecreta')
@login_required
def listasecreta():
    try:
        conn=cnx.mysql.connect()
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM T_Lecturas')
        data=cursor.fetchall()
        listaVO=[]
        for fila in data:
            listaVO.append(fila)
    except Exception as e:
        return json.dumps({'error':str(e)})
    finally: 
        cursor.close()
        conn.close()
    return render_template('listasecreta.html', eventos=listaVO)

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith( '.html' ):
            template += '.html'

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( template, segment=segment )

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500

# Helper - Extract current page name from request 
def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
