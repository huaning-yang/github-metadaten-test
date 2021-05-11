# github-metadaten-test

Repository List
{% for repository in site.github.public_repositories %}

    [{{ repository.name }}]({{ repository.html_url }})
    [{{ repository.contributors_url }}]
    {{repository.releases_url}}
    Release:
    {{repository.release}}
{% endfor %}

{{site.github.releases_url}}

Release:
{{site.github.release}}

Latest releases:
{{site.github.latest_release}}

}