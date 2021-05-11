# github-metadaten-test

Repository List
{% for repository in site.github.public_repositories %}

    [{{ repository.name }}]({{ repository.html_url }})
    [{{ repository.contributors_url }}]

{% endfor %}

{{site.github.releases_url}}

Latest releases:
{{site.github.latest_release.html_url}} 

{{site.github.latest_release.tag_name}}

{{site.github.latest_release.name}}

Site.github:
{{site.github}}