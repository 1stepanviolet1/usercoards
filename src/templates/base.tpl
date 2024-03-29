<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi"
      crossorigin="anonymous"
    />
    <link type="text/css" rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}" />
    
    {% if title %}
    <title> {{ title }} </title>
    {% else %}
    <title> Default title </title>
    {% endif %}
  </head>
  <body>
    <div class="container">
    {% block content %}



    {% endblock %}
    </div>
  </body>
  <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</html>
