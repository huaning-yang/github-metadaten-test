# github-metadaten-test

Repository List
{% for repository in site.github.public_repositories %}

        [{{ repository.name }}]({{ repository.html_url }}) 
{% endfor %}


Latest releases:
{% for latest_release in site.github.latest_release %}
    {{latest_release}}
{% endfor %}

Repo Object
{% for repository in site.github.public_repositories %}
    {{repository}}
{% endfor %}

Repo List 2
{% for repository in site.github.public_repositories %}
    {% for latest_release in repository.latest_release %}
        {{latest_release.assets_url}}
    {% endfor %}
{% endfor %}