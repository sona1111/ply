"""
Example:
sidebar = {
  "mname":"community",
  "label":"Community",
  "icon":"fa-solid fa-users-rectangle",
  "url":"communities.community/",
  "js":"/static/js/forge_create-community.js",
  "menu":[
    {"url":"forge/edit/community/cover","label":"Community Details",'icon':'fa-solid fa-user-group','onclick':''},
    {"url":"forge/script/studio","label":"PLYScript Studio",'icon':'fa-solid fa-star','onclick':''},
    {"url":"communities.community/staff","label":"Staff Management",'icon':'fa-solid fa-user-tie'},
    {"url":"communities.community/admins","label":"Admin Management",'icon':'fa-solid fa-screwdriver-wrench'},

    ]
  }
"""
sidebar =  {
  "mname":"dashboards",
  "label":"Dashboards",
  "icon":"fa-solid fa-gauge",
  "url":"communities.dashboards/",
  "js":"/static/communities.dashboards/js/dashboards.js",
  "menu":[
    {"url":"forge/edit/dashboard/editor","label":"Dashboard Studio",'icon':'fa-solid fa-paintbrush','onclick':''}

    ]
  }