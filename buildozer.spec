[app]

title = TestCamera
package.name = testcamera
package.domain = org.hajihaji6765

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy
android.permissions = CAMERA
orientation = portrait
fullscreen = 0

android.api = 35
android.minapi = 21
android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1
