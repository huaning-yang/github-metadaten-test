# github-metadaten-test

Repository List
{% for repository in site.github.public_repositories %}

    [{{ repository.name }}]({{ repository.html_url }})
    [{{ repository.contributors_url }}]
{% endfor %}


Latest releases:
{{site.github.latest_release}}

Repo List 2
{% for repository in site.github.public_repositories %}

        {{repository}}
{% endfor %}