<div align="center">
  <h1>Welcome to Ply.</h1>
</div>

<div align="center">
  <!-- breaks if we dont have this blank line -->
  
  <a href="">![GitHub contributors](https://img.shields.io/github/contributors-anon/mistressAlisi/ply?style=for-the-badge)</a>
  <a href="">![GitHub issues](https://img.shields.io/github/issues/mistressAlisi/ply?style=for-the-badge)</a>
</div>

<h4 align="center">
  Nerdy name aside; Ply is a toolkit and platform to rapidly create, implement and customise websites and webapps that have Social, Sharing, and RolePlaying components.
</h4>
<hr/>
<h3 align="center">--Design Philosphy--</h3>
<p align="center">The application is built mostly with Python and Django. It makes heavy use of PostgreSQL and some neat features like PL/pgSQL for the backend: The philosophy behind the backend is to "make it as simple and efficient as possible" - one of the ways we do that is by keeping processing of data to the minimum level possible, and by reducing all not needed loops for data algos. PL/pgSQL helps us greatly in doing a lot of lifting inside the database itself to keep the Django Engine highly performant and responsive. Ply scales very well using UWSGI/Gunicorn (we test using UWSGI) and NGINX. Several key concepts that Ply relies on are explained below:
</p>

<h3 align="center">--Introduction--</h3>
<p align="center">Ply is highly flexible and can be used in an infinite number of configurations to host Communites, Websites, Galleries, Role Playing games that use Pen and Paper information, and in the future, Second Life-based Roleplaying using an integrated HUD we call PlyHUD (under development.)
</p>

<p align="center">The application is built mostly with Python and Django. It makes heavy use of PostgreSQL and some neat features like PL/pgSQL for the backend: The philosophy behind the backend is to "make it as simple and efficient as possible" - one of the ways we do that is by keeping processing of data to the minimum level possible, and by reducing all not needed loops for data algos. PL/pgSQL helps us greatly in doing a lot of lifting inside the database itself to keep the Django Engine highly performant and responsive. Ply scales very well using UWSGI/Gunicorn (we test using UWSGI) and NGINX. Several key concepts that Ply relies on are explained below:
</p>



<h3 align="center">--Core Ply features--</h3>
<p align="center">By design, Ply is highly customisable and extensible. It relies on the Django philosophy of keeping individual "Apps" (or services) in their own separate modules inside the main ply namespace. The following modules are provided and under active development:
<ol>
<li><strong>"Almanac":</strong> A dynamic webpage and blogging service that closely resembles a CRM, with customisable, user-editable pages and menus.</li>
</ol>
</p>


