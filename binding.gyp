{
  'targets': [
    {
      'target_name': 'flexml-js',
      'sources': [
        'flexml/src/AppBase.cpp',
        'flexml/src/API.cpp',
        'flexml/src/AppAPI.cpp',
        'flexml/src/AppAPIInternal.cpp',
        'flexml/src/MLAPI.cpp',
       ],
      'link_settings': {
        'libraries': [
          '<!@(pkg-config glib-2.0 --libs)',
          '<!@(pkg-config dbus-1 --libs)',
          "-L<(PRODUCT_DIR)/../../out/libs -lant-cmfw",
          "-L<(PRODUCT_DIR)/../../out/libs -lant-message"
        ],
        'ldflags': [
          '-Wl,-rpath'
        ]
      },
      'include_dirs': [
        'flexml/inc',
        'message/inc',
        'communication/inc',
        '<!@(pkg-config glib-2.0 --cflags-only-I | sed s/-I//g)',
        '<!@(pkg-config dbus-1 --cflags-only-I | sed s/-I//g)'
      ]
    }
  ]
}
