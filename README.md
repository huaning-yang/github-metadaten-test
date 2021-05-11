# github-metadaten-test

Repository List
{% for repository in site.github.public_repositories %}

        [{{ repository.name }}]({{ repository.html_url }})
{% endfor %}


Latest releases:
{% for latest in site.github.latest_release %}
    {{latest.html_url}}
    {{latest.tag_name}}
    {{latest.release_name}}
    {{latest.assets}}
{% endfor %}

