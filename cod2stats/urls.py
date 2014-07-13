urls = (
    '^/', 'cod2stats.views.Index',
    '^/players', 'cod2stats.views.Players',
    '^/player/(\d+)', 'cod2stats.views.Player',
    '^/rounds', 'cod2stats.views.Rounds',
    '^/round/(\d+)', 'cod2stats.views.Round',
)
