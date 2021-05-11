# github-metadaten-test

Repository List
{% for repository in site.github.public_repositories %}

    [{{ repository.name }}]({{ repository.html_url }})
    [{{ repository.contributors_url }}]
{% endfor %}

{{site.github.owner_name}}

Latest releases:
{{site.github.latest_release}}

}