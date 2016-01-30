import sublime, sublime_plugin

class MinifyOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):
        file_types_to_minify = ['js', 'css']
        not_minify = ['min']
        file_name_parts = view.file_name().split('.')
        if file_name_parts[-1:] in file_types_to_minify and file_name_parts[-2:-1] not in not_minify:
            view.run_command('minify_to_file')
