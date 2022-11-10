# Configure nginx to process all requests
exec {'24: Too many open files':
  command => 'sed -i "s/15/4098/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->
exec {'Restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
