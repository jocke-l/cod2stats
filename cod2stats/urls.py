urls = (
    '^/', 'cod2stats.views.Index',
    '^/players', 'cod2stats.views.Players',
    '^/player/(\d+)', 'cod2stats.views.Player',
    '^/round/(\d+)', 'cod2stats.views.Round',
)
