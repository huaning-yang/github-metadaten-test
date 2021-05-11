# github-metadaten-test

Repository List
{% for repository in site.github.public_repositories %}

        [{{ repository.name }}]({{ repository.html_url }}) 
{% endfor %}


Latest releases:
{% for latest_release in site.github.latest_releases %}
    {{latest_release}}
    {{latest_release.name}}
{% endfor %}