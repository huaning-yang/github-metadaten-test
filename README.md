# github-metadaten-test

Repository List
{% for repository in site.github.public_repositories %}

    [{{ repository.name }}]({{ repository.html_url }})
    [{{ repository.contributors_url }}]
    {{repository.releases_html_url}}
{% endfor %}

{{site.github.releases_url}}

Latest releases:
{{site.github.latest_release}}

}