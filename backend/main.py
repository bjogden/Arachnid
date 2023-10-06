from flask import (
    Flask, 
    redirect,
    render_template, 
    request,
    url_for,
)

from .config import FlaskConfig
from .forms import ArachnidForm


app = Flask(__name__)
app.config.from_object(FlaskConfig)


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ArachnidForm()
    if form.validate_on_submit():
        # form.screen_width.data
        # form.screen_height.data
        urls = set(form.urls.data.replace('\r', '').split('\n'))
        # Create two tables: 
        # ...Scrape (id: PK unique int, job_id: FK int, link: str, image_path: str)
        # ...Job (id: PK unique int)

        # All links get added to Scrape table.
        # Each POST creates new Job to which all Scrape records are tied.

        # "urls" `url_for` kwarg is changed to job_id.
        # Add temporary redirect page to show loading?
        # When done loading, redirect to /success w/ job_id like below 
        # which will query from database.
        return redirect(url_for('success', urls='|'.join(urls)))

    return render_template('home.html', form=form)


@app.route('/success')
def success():
    urls = request.args.get('urls') or None
    # Query from database based on proposed "job_id" query param to get
    # all Scrape records with links and the associated scrape images.
    if urls:
        urls = urls.split('|')

    print(urls)
    print(type(urls))
    return render_template('success.html', urls=urls)
