import base64 #Пытаешься Розсекретить мой код = дура)
base64_string = "aW1wb3J0IG9zCmltcG9ydCByZQpmcm9tIHl0X2RscCBpbXBvcnQgWW91dHViZURMCmZyb20gY29sb3JhbWEgaW1wb3J0IGluaXQsIEZvcmUsIFN0eWxlCmZyb20gdGltZSBpbXBvcnQgc2xlZXAKCmluaXQoYXV0b3Jlc2V0PVRydWUpCgpLRVkgPSAiSEFLQUhaS1FJRUlXTzkwMjAzMDMwMzAzMDMwMzkzOTkzOTM5MzkzOTM5MzkzMzMzNDQ0MzU2NjU2NjU1NTU1NTQ0NDQ2NjgzOTM5MzkzOTIwOTI3MzczOTEwMDEwMzk0ODQ3Mzg5MzkyOTM3Mzc4MzkyOTI5MzgzODgzODI5MjkzOTM5Mzk5M0Eyckp0OG5Ea1BxTG1XNXZYejFvUWY5c05jQjdZYkUzUmpWd0Z6OFRnVW9Ia0E2V3BMbTBKdlh0VXo5ZVJnVVRCUldFQkZSRUUiClZBTElEX0tFWVMgPSBbS0VZXQpUQVJHRVRfVkVSU0lPTiA9IDEuMgoKZG93bmxvYWRfcGF0aCA9ICIvc3RvcmFnZS9lbXVsYXRlZC8wL1lUdWJlL1lUVmlkZW8iCmF1ZGlvX3BhdGggPSAiL3N0b3JhZ2UvZW11bGF0ZWQvMC9ZVHViZS9BdWRpb1lUIgp2ZXJzaW9uX2ZpbGUgPSAidmVyc2lvbi50eHQiCgpkZWYgY2xlYXJfc2NyZWVuKCk6CiAgICBvcy5zeXN0ZW0oJ2NscycgaWYgb3MubmFtZSA9PSAnbnQnIGVsc2UgJ2NsZWFyJykKCmRlZiBib2xkKHRleHQpOgogICAgcmV0dXJuIGYiXDAzM1sxbXt0ZXh0fVwwMzNbMG0iCgpkZWYgY29sb3JlZCh0ZXh0LCBjb2xvcik6CiAgICByZXR1cm4gZiJ7Y29sb3J9e3RleHR9e1N0eWxlLlJFU0VUX0FMTH0iCgpkZWYgY2hlY2tfa2V5KCk6CiAgICBjbGVhcl9zY3JlZW4oKQogICAgcHJpbnQoYm9sZChjb2xvcmVkKCLwn5SQINCf0YDQvtCy0LXRgNC60LAg0LTQvtGB0YLRg9C/0LAuLi4iLCBGb3JlLkdSRUVOKSkpCiAgICBrZXkgPSBpbnB1dChib2xkKGNvbG9yZWQoIvCflJEg0JLQstC10LTQuNGC0LUg0LrQu9GO0Ycg0LTQu9GPINC00L7RgdGC0YPQv9CwOiAiLCBGb3JlLllFTExPVykpKQogICAgaWYga2V5IG5vdCBpbiBWQUxJRF9LRVlTOgogICAgICAgIHByaW50KGJvbGQoY29sb3JlZCgi4puUINCd0LXQstC10YDQvdGL0Lkg0JrQu9GO0YcuIiwgRm9yZS5SRUQpKSkKICAgICAgICBleGl0KCkKICAgIGVsc2U6CiAgICAgICAgcHJpbnQoYm9sZChjb2xvcmVkKCLinIUg0JTQvtGB0YLRg9C/INGA0LDQt9GA0LXRiNC10L0uINCa0LvRjtGHINC/0YDQuNC90Y/RgiEiLCBGb3JlLkdSRUVOKSkpCiAgICBpbnB1dChib2xkKGNvbG9yZWQoIlxu8J+agCDQndCw0LbQvNC40YLQtSBFbnRlciDQtNC70Y8g0L/RgNC+0LTQvtC70LbQtdC90LjRjy4uLiIsIEZvcmUuWUVMTE9XKSkpCgpkZWYgaXNfeW91dHViZV91cmwodXJsKToKICAgIHlvdXR1YmVfcmVnZXggPSByJyhodHRwcz86Ly8pPyh3d3dcLik/KHlvdXR1YmV8eW91dHV8eW91dHViZS1ub2Nvb2tpZSlcLihjb218YmUpLycKICAgIHJldHVybiByZS5tYXRjaCh5b3V0dWJlX3JlZ2V4LCB1cmwpIGlzIG5vdCBOb25lCgpkZWYgcHJpbnRfbWVkaWFfZGV0YWlscyhpbmZvKToKICAgIHRpdGxlID0gaW5mby5nZXQoJ3RpdGxlJywgJ9Cd0LXQuNC30LLQtdGB0YLQvdC+0LUg0L3QsNC30LLQsNC90LjQtScpCiAgICBkdXJhdGlvbiA9IGluZm8uZ2V0KCdkdXJhdGlvbicsIDApCiAgICBmaWxlc2l6ZSA9IG9zLnBhdGguZ2V0c2l6ZShpbmZvWydmaWxlbmFtZSddKSAvLyAoMTAyNCAqIDEwMjQpCiAgICBwcmludChib2xkKGNvbG9yZWQoZiJcbvCfjp4g0J3QsNC30LLQsNC90LjQtToge3RpdGxlfSIsIEZvcmUuR1JFRU4pKSkKICAgIHByaW50KGJvbGQoY29sb3JlZChmIuKPsyDQlNC70LjRgtC10LvRjNC90L7RgdGC0Yw6IHtkdXJhdGlvbiAvLyA2MH0g0LzQuNC90YPRgiB7ZHVyYXRpb24gJSA2MH0g0YHQtdC60YPQvdC0IiwgRm9yZS5DWUFOKSkpCiAgICBwcmludChib2xkKGNvbG9yZWQoZiLwn5K+INCg0LDQt9C80LXRgDoge2ZpbGVzaXplfU1CIiwgRm9yZS5NQUdFTlRBKSkpCgpkZWYgZG93bmxvYWRfdmlkZW8oeXRfbGluaywgcXVhbGl0eT0nYmVzdFtoZWlnaHQ8PTQ4MF0nKToKICAgIHlkbF9vcHRzID0gewogICAgICAgICdmb3JtYXQnOiBxdWFsaXR5LAogICAgICAgICdvdXR0bXBsJzogJyUodGl0bGUpcy4lKGV4dClzJywKICAgICAgICAncXVpZXQnOiBUcnVlLAogICAgICAgICdub193YXJuaW5ncyc6IFRydWUsCiAgICAgICAgJ25vX3Byb2dyZXNzJzogVHJ1ZSwKICAgICAgICAnbm9wbGF5bGlzdCc6IFRydWUsCiAgICAgICAgJ3dyaXRlaW5mb2pzb24nOiBUcnVlLAogICAgfQoKICAgIG9zLm1ha2VkaXJzKGRvd25sb2FkX3BhdGgsIGV4aXN0X29rPVRydWUpCiAgICB5ZGxfb3B0c1snb3V0dG1wbCddID0gb3MucGF0aC5qb2luKGRvd25sb2FkX3BhdGgsIHlkbF9vcHRzWydvdXR0bXBsJ10pCgogICAgdHJ5OgogICAgICAgIHdpdGggWW91dHViZURMKHlkbF9vcHRzKSBhcyB5ZGw6CiAgICAgICAgICAgIHByaW50KGJvbGQoY29sb3JlZCgi8J+OpSDQndCw0YfQuNC90LDRjiDRgdC60LDRh9C40LLQsNC90LjQtSDQstC40LTQtdC+Li4uIiwgRm9yZS5DWUFOKSkpCiAgICAgICAgICAgIGluZm8gPSB5ZGwuZXh0cmFjdF9pbmZvKHl0X2xpbmssIGRvd25sb2FkPVRydWUpCiAgICAgICAgICAgIGZpbGVuYW1lID0geWRsLnByZXBhcmVfZmlsZW5hbWUoaW5mbykKICAgICAgICAgICAgcHJpbnRfbWVkaWFfZGV0YWlscyh7J2ZpbGVuYW1lJzogZmlsZW5hbWUsICoqaW5mb30pCiAgICAgICAgICAgIHByaW50KGJvbGQoY29sb3JlZChmIlxu8J+OiSDQktC40LTQtdC+INGD0YHQv9C10YjQvdC+INGB0LrQsNGH0LDQvdC+OiB7ZmlsZW5hbWV9IiwgRm9yZS5HUkVFTikpKQoKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICBwcmludChib2xkKGNvbG9yZWQoZiLinZcg0J7RiNC40LHQutCwOiB7c3RyKGUpfSIsIEZvcmUuUkVEKSkpCgogICAgaW5wdXQoYm9sZChjb2xvcmVkKCJcbuKeoSDQndCw0LbQvNC40YLQtSBFbnRlciDQtNC70Y8g0L/RgNC+0LTQvtC70LbQtdC90LjRjy4uLiIsIEZvcmUuWUVMTE9XKSkpCgpkZWYgZG93bmxvYWRfYXVkaW8oeXRfbGluayk6CiAgICB5ZGxfb3B0cyA9IHsKICAgICAgICAnZm9ybWF0JzogJ2Jlc3RhdWRpby9iZXN0JywKICAgICAgICAnb3V0dG1wbCc6ICclKHRpdGxlKXMuJShleHQpcycsCiAgICAgICAgJ3Bvc3Rwcm9jZXNzb3JzJzogW3sKICAgICAgICAgICAgJ2tleSc6ICdGRm1wZWdFeHRyYWN0QXVkaW8nLAogICAgICAgICAgICAncHJlZmVycmVkY29kZWMnOiAnbXAzJywKICAgICAgICAgICAgJ3ByZWZlcnJlZHF1YWxpdHknOiAnMTkyJywKICAgICAgICB9XSwKICAgICAgICAncXVpZXQnOiBUcnVlLAogICAgICAgICdub193YXJuaW5ncyc6IFRydWUsCiAgICAgICAgJ25vX3Byb2dyZXNzJzogVHJ1ZSwKICAgIH0KCiAgICBvcy5tYWtlZGlycyhhdWRpb19wYXRoLCBleGlzdF9vaz1UcnVlKQogICAgeWRsX29wdHNbJ291dHRtcGwnXSA9IG9zLnBhdGguam9pbihhdWRpb19wYXRoLCB5ZGxfb3B0c1snb3V0dG1wbCddKQoKICAgIHRyeToKICAgICAgICB3aXRoIFlvdXR1YmVETCh5ZGxfb3B0cykgYXMgeWRsOgogICAgICAgICAgICBwcmludChib2xkKGNvbG9yZWQoIvCfjqcg0J3QsNGH0LjQvdCw0Y4g0YHQutCw0YfQuNCy0LDQvdC40LUg0LDRg9C00LjQvi4uLiIsIEZvcmUuQ1lBTikpKQogICAgICAgICAgICBpbmZvID0geWRsLmV4dHJhY3RfaW5mbyh5dF9saW5rLCBkb3dubG9hZD1UcnVlKQogICAgICAgICAgICBmaWxlbmFtZSA9IHlkbC5wcmVwYXJlX2ZpbGVuYW1lKGluZm8pCiAgICAgICAgICAgIHByaW50X21lZGlhX2RldGFpbHMoeydmaWxlbmFtZSc6IGZpbGVuYW1lLCAqKmluZm99KQogICAgICAgICAgICBwcmludChib2xkKGNvbG9yZWQoZiJcbvCfjrYg0JDRg9C00LjQviDRg9GB0L/QtdGI0L3QviDRgdC60LDRh9Cw0L3Qvjoge2ZpbGVuYW1lfSIsIEZvcmUuR1JFRU4pKSkKCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgcHJpbnQoYm9sZChjb2xvcmVkKGYi4p2XINCe0YjQuNCx0LrQsDoge3N0cihlKX0iLCBGb3JlLlJFRCkpKQoKICAgIGlucHV0KGJvbGQoY29sb3JlZCgiXG7inqEg0J3QsNC20LzQuNGC0LUgRW50ZXIg0LTQu9GPINC/0YDQvtC00L7Qu9C20LXQvdC40Y8uLi4iLCBGb3JlLllFTExPVykpKQoKZGVmIGNoZWNrX2Zvcl91cGRhdGVzKCk6CiAgICBpZiBub3Qgb3MucGF0aC5leGlzdHModmVyc2lvbl9maWxlKToKICAgICAgICB3aXRoIG9wZW4odmVyc2lvbl9maWxlLCAndycpIGFzIGY6CiAgICAgICAgICAgIGYud3JpdGUoJzBcbicpCgogICAgd2l0aCBvcGVuKHZlcnNpb25fZmlsZSwgJ3InKSBhcyBmOgogICAgICAgIGN1cnJlbnRfdmVyc2lvbiA9IGludChmLnJlYWQoKS5zdHJpcCgpKQoKICAgIGlmIGN1cnJlbnRfdmVyc2lvbiA8IFRBUkdFVF9WRVJTSU9OOgogICAgICAgIHByaW50KGJvbGQoY29sb3JlZChmIvCflIQg0J7QsdC90L7QstC70LXQvdC40LUg0LTQviDQstC10YDRgdC40Lgge1RBUkdFVF9WRVJTSU9OfS4uLiIsIEZvcmUuWUVMTE9XKSkpCiAgICAgICAgd2l0aCBvcGVuKHZlcnNpb25fZmlsZSwgJ3cnKSBhcyBmOgogICAgICAgICAgICBmLndyaXRlKHN0cihUQVJHRVRfVkVSU0lPTikpCiAgICAgICAgcHJpbnQoYm9sZChjb2xvcmVkKCLinIUg0J7QsdC90L7QstC70LXQvdC40LUg0LfQsNCy0LXRgNGI0LXQvdC+LiIsIEZvcmUuR1JFRU4pKSkKCmRlZiBtYWluX21lbnUoKToKICAgIGNsZWFyX3NjcmVlbigpCiAgICBwcmludChib2xkKGNvbG9yZWQoIiIiCiAgICDilojilojilZcgICDilojilojilZfilojilojilojilojilojilojilojilojilZfilojilojilojilojilojilojilZcg4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKVlyAgICDilojilojilZfilojilojilojilojilojilojilojilZfilojilojilojilojilojilojilZcgCiAgICDilojilojilZEgICDilojilojilZHilZrilZDilZDilojilojilZTilZDilZDilZ3ilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilojilojilZfilojilojilZEgICAg4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4pWQ4pWQ4pWd4paI4paI4pWU4pWQ4pWQ4paI4paI4pWXCiAgICDilojilojilZEgICDilojilojilZEgICDilojilojilZEgICDilojilojilojilojilojilojilZTilZ3ilojilojilojilojilojilojilZTilZ3ilojilojilZEg4paI4pWXIOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4paI4paI4paI4paI4pWU4pWdCiAgICDilojilojilZEgICDilojilojilZEgICDilojilojilZEgICDilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilojilojilZfilojilojilZHilojilojilojilZfilojilojilZHilojilojilZTilZDilZDilZ0gIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVlwogICAg4pWa4paI4paI4paI4paI4paI4paI4pWU4pWdICAg4paI4paI4pWRICAg4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4pWRICDilojilojilZHilZrilojilojilojilZTilojilojilojilZTilZ3ilojilojilojilojilojilojilojilZfilojilojilojilojilojilojilZTilZ0KICAgICDilZrilZDilZDilZDilZDilZDilZ0gICAg4pWa4pWQ4pWdICAg4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWdIOKVmuKVkOKVnSAg4pWa4pWQ4pWdIOKVmuKVkOKVkOKVneKVmuKVkOKVkOKVnSDilZrilZDilZDilZDilZDilZDilZDilZ3ilZrilZDilZDilZDilZDilZDilZ0KICAKICAgIENyZWF0b3I6IEBpZmFtZV9vZmZpY2lhbAogICAgCiAgICBWZXJzaW9uOiAyLjIKICAgIAogICAgIiIiLCBGb3JlLlJFRCkpKQogICAgcHJpbnQoYm9sZChjb2xvcmVkKCLwn5S5IFlvdVR1YmUgRG93bmxvYWRlciIsIEZvcmUuR1JFRU4pKSkKICAgIHByaW50KGJvbGQoY29sb3JlZCgiMS4g0KHQutCw0YfQuNCy0LDQvdC40LUg0LLQuNC00LXQviIsIEZvcmUuQ1lBTikpKQogICAgcHJpbnQoYm9sZChjb2xvcmVkKCIyLiDQodC60LDRh9C40LLQsNC90LjQtSDQsNGD0LTQuNC+IiwgRm9yZS5DWUFOKSkpCiAgICBwcmludChib2xkKGNvbG9yZWQoIjAuINCS0YvRhdC+0LQiLCBGb3JlLlJFRCkpKQoKZGVmIG1haW4oKToKICAgIGNoZWNrX2tleSgpCiAgICBjaGVja19mb3JfdXBkYXRlcygpCgogICAgd2hpbGUgVHJ1ZToKICAgICAgICBtYWluX21lbnUoKQogICAgICAgIGNob2ljZSA9IGlucHV0KGJvbGQoY29sb3JlZCgiIOKeodCS0YvQsdC10YDQuNGC0LUg0L7Qv9GG0LjRjjogIiwgRm9yZS5ZRUxMT1cpKSkuc3RyaXAoKQoKICAgICAgICBpZiBjaG9pY2UgPT0gJzEnOgogICAgICAgICAgICB5dF9saW5rID0gaW5wdXQoYm9sZChjb2xvcmVkKCLwn5SXINCS0LLQtdC00LjRgtC1IFVSTCDQstC40LTQtdC+OiAiLCBGb3JlLllFTExPVykpKS5zdHJpcCgpCiAgICAgICAgICAgIGlmIGlzX3lvdXR1YmVfdXJsKHl0X2xpbmspOgogICAgICAgICAgICAgICAgZG93bmxvYWRfdmlkZW8oeXRfbGluaykKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIHByaW50KGJvbGQoY29sb3JlZCgi4p2MINCd0LXQstC10YDQvdGL0LkgVVJMIiwgRm9yZS5SRUQpKSkKCiAgICAgICAgZWxpZiBjaG9pY2UgPT0gJzInOgogICAgICAgICAgICB5dF9saW5rID0gaW5wdXQoYm9sZChjb2xvcmVkKCLwn5SXINCS0LLQtdC00LjRgtC1IFVSTCDQstC40LTQtdC+OiAiLCBGb3JlLllFTExPVykpKS5zdHJpcCgpCiAgICAgICAgICAgIGlmIGlzX3lvdXR1YmVfdXJsKHl0X2xpbmspOgogICAgICAgICAgICAgICAgZG93bmxvYWRfYXVkaW8oeXRfbGluaykKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIHByaW50KGJvbGQoY29sb3JlZCgi4p2MINCd0LXQstC10YDQvdGL0LkgVVJMIiwgRm9yZS5SRUQpKSkKCiAgICAgICAgZWxpZiBjaG9pY2UgPT0gJzAnOgogICAgICAgICAgICBwcmludChib2xkKGNvbG9yZWQoIvCfkYsg0JLRi9GF0L7QtCDQuNC3INC/0YDQvtCz0YDQsNC80LzRiy4iLCBGb3JlLllFTExPVykpKQogICAgICAgICAgICBicmVhawoKICAgICAgICBlbHNlOgogICAgICAgICAgICBwcmludChib2xkKGNvbG9yZWQoIuKdlyDQndC10LLQtdGA0L3Ri9C5INCy0YvQsdC+0YAuINCf0L7Qv9GA0L7QsdGD0LnRgtC1INGB0L3QvtCy0LAuIiwgRm9yZS5SRUQpKSkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCk="
decoded_bytes = base64.b64decode(base64_string)
decoded_string = decoded_bytes.decode('utf-8')
exec(decoded_string)
