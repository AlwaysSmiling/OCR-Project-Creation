from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import base64
import json
import os
import imageedit
import io

os.chdir('E:\Python Projects\Hindi OCR')

HOST_ADDRESS = ""
HOST_PORT = 8000

def runocr(param1, param2, param3):
    param2 = param2.replace(b'data:image/png;base64,', b'', 1)
    with io.open("srcraw.png", "wb") as fh:
        fh.write(base64.decodebytes(param2))
    crop_data = json.loads(param3)
    imageedit.run(crop_data)
    param1 = param1.replace('%20', ' ' , 2)
    param1 = param1.replace('/', ' ', 1)
    os.system('python' + param1)
    return
    

class RequestHandler(SimpleHTTPRequestHandler):
          
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body_text = self.rfile.read(content_length)
        body_data = body_text.split()
        runocr(self.path, body_data[0], body_data[1])
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'done')    
  
def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    """ follows example shown on docs.python.org """
    server_address = (HOST_ADDRESS, HOST_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run(handler_class=RequestHandler)


#class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
#
#    """Simple HTTP request handler with GET and HEAD commands.
#    This serves files from the current directory and any of its
#    subdirectories.  The MIME type for files is determined by
#    calling the .guess_type() method.
#    The GET and HEAD requests are identical except that the HEAD
#    request omits the actual contents of the file.
#    """
#
#    server_version = "SimpleHTTP/" + __version__
#
#    def __init__(self, *args, directory=None, **kwargs):
#        if directory is None:
#            directory = os.getcwd()
#        self.directory = directory
#        super().__init__(*args, **kwargs)
#
#    def do_GET(self):
#        """Serve a GET request."""
#        f = self.send_head()
#        if f:
#            try:
#                self.copyfile(f, self.wfile)
#            finally:
#                f.close()
#
#    def do_HEAD(self):
#        """Serve a HEAD request."""
#        f = self.send_head()
#        if f:
#            f.close()
#
#    def send_head(self):
#        """Common code for GET and HEAD commands.
#        This sends the response code and MIME headers.
#        Return value is either a file object (which has to be copied
#        to the outputfile by the caller unless the command was HEAD,
#        and must be closed by the caller under all circumstances), or
#        None, in which case the caller has nothing further to do.
#        """
#        path = self.translate_path(self.path)
#        f = None
#        if os.path.isdir(path):
#            parts = urllib.parse.urlsplit(self.path)
#            if not parts.path.endswith('/'):
#                # redirect browser - doing basically what apache does
#                self.send_response(HTTPStatus.MOVED_PERMANENTLY)
#                new_parts = (parts[0], parts[1], parts[2] + '/',
#                             parts[3], parts[4])
#                new_url = urllib.parse.urlunsplit(new_parts)
#                self.send_header("Location", new_url)
#                self.end_headers()
#                return None
#            for index in "index.html", "index.htm":
#                index = os.path.join(path, index)
#                if os.path.exists(index):
#                    path = index
#                    break
#            else:
#                return self.list_directory(path)
#        ctype = self.guess_type(path)
#        try:
#            f = open(path, 'rb')
#        except OSError:
#            self.send_error(HTTPStatus.NOT_FOUND, "File not found")
#            return None
#
#        try:
#            fs = os.fstat(f.fileno())
#            # Use browser cache if possible
#            if ("If-Modified-Since" in self.headers
#                    and "If-None-Match" not in self.headers):
#                # compare If-Modified-Since and time of last file modification
#                try:
#                    ims = email.utils.parsedate_to_datetime(
#                        self.headers["If-Modified-Since"])
#                except (TypeError, IndexError, OverflowError, ValueError):
#                    # ignore ill-formed values
#                    pass
#                else:
#                    if ims.tzinfo is None:
#                        # obsolete format with no timezone, cf.
#                        # https://tools.ietf.org/html/rfc7231#section-7.1.1.1
#                        ims = ims.replace(tzinfo=datetime.timezone.utc)
#                    if ims.tzinfo is datetime.timezone.utc:
#                        # compare to UTC datetime of last modification
#                        last_modif = datetime.datetime.fromtimestamp(
#                            fs.st_mtime, datetime.timezone.utc)
#                        # remove microseconds, like in If-Modified-Since
#                        last_modif = last_modif.replace(microsecond=0)
#
#                        if last_modif <= ims:
#                            self.send_response(HTTPStatus.NOT_MODIFIED)
#                            self.end_headers()
#                            f.close()
#                            return None
#
#            self.send_response(HTTPStatus.OK)
#            self.send_header("Content-type", ctype)
#            self.send_header("Content-Length", str(fs[6]))
#            self.send_header("Last-Modified",
#                self.date_time_string(fs.st_mtime))
#            self.end_headers()
#            return f
#        except:
#            f.close()
#            raise
#
#    def list_directory(self, path):
#        """Helper to produce a directory listing (absent index.html).
#        Return value is either a file object, or None (indicating an
#        error).  In either case, the headers are sent, making the
#        interface the same as for send_head().
#        """
#        try:
#            list = os.listdir(path)
#        except OSError:
#            self.send_error(
#                HTTPStatus.NOT_FOUND,
#                "No permission to list directory")
#            return None
#        list.sort(key=lambda a: a.lower())
#        r = []
#        try:
#            displaypath = urllib.parse.unquote(self.path,
#                                               errors='surrogatepass')
#        except UnicodeDecodeError:
#            displaypath = urllib.parse.unquote(path)
#        displaypath = html.escape(displaypath, quote=False)
#        enc = sys.getfilesystemencoding()
#        title = 'Directory listing for %s' % displaypath
#        r.append('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
#                 '"http://www.w3.org/TR/html4/strict.dtd">')
#        r.append('<html>\n<head>')
#        r.append('<meta http-equiv="Content-Type" '
#                 'content="text/html; charset=%s">' % enc)
#        r.append('<title>%s</title>\n</head>' % title)
#        r.append('<body>\n<h1>%s</h1>' % title)
#        r.append('<hr>\n<ul>')
#        for name in list:
#            fullname = os.path.join(path, name)
#            displayname = linkname = name
#            # Append / for directories or @ for symbolic links
#            if os.path.isdir(fullname):
#                displayname = name + "/"
#                linkname = name + "/"
#            if os.path.islink(fullname):
#                displayname = name + "@"
#                # Note: a link to a directory displays with @ and links with /
#            r.append('<li><a href="%s">%s</a></li>'
#                    % (urllib.parse.quote(linkname,
#                                          errors='surrogatepass'),
#                       html.escape(displayname, quote=False)))
#        r.append('</ul>\n<hr>\n</body>\n</html>\n')
#        encoded = '\n'.join(r).encode(enc, 'surrogateescape')
#        f = io.BytesIO()
#        f.write(encoded)
#        f.seek(0)
#        self.send_response(HTTPStatus.OK)
#        self.send_header("Content-type", "text/html; charset=%s" % enc)
#        self.send_header("Content-Length", str(len(encoded)))
#        self.end_headers()
#        return f
#
#    def translate_path(self, path):
#        """Translate a /-separated PATH to the local filename syntax.
#        Components that mean special things to the local file system
#        (e.g. drive or directory names) are ignored.  (XXX They should
#        probably be diagnosed.)
#        """
#        # abandon query parameters
#        path = path.split('?',1)[0]
#        path = path.split('#',1)[0]
#        # Don't forget explicit trailing slash when normalizing. Issue17324
#        trailing_slash = path.rstrip().endswith('/')
#        try:
#            path = urllib.parse.unquote(path, errors='surrogatepass')
#        except UnicodeDecodeError:
#            path = urllib.parse.unquote(path)
#        path = posixpath.normpath(path)
#        words = path.split('/')
#        words = filter(None, words)
#        path = self.directory
#        for word in words:
#            if os.path.dirname(word) or word in (os.curdir, os.pardir):
#                # Ignore components that are not a simple file/directory name
#                continue
#            path = os.path.join(path, word)
#        if trailing_slash:
#            path += '/'
#        return path
#
#    def copyfile(self, source, outputfile):
#        """Copy all data between two file objects.
#        The SOURCE argument is a file object open for reading
#        (or anything with a read() method) and the DESTINATION
#        argument is a file object open for writing (or
#        anything with a write() method).
#        The only reason for overriding this would be to change
#        the block size or perhaps to replace newlines by CRLF
#        -- note however that this the default server uses this
#        to copy binary data as well.
#        """
#        shutil.copyfileobj(source, outputfile)
#
#    def guess_type(self, path):
#        """Guess the type of a file.
#        Argument is a PATH (a filename).
#        Return value is a string of the form type/subtype,
#        usable for a MIME Content-type header.
#        The default implementation looks the file's extension
#        up in the table self.extensions_map, using application/octet-stream
#        as a default; however it would be permissible (if
#        slow) to look inside the data to make a better guess.
#        """
#
#        base, ext = posixpath.splitext(path)
#        if ext in self.extensions_map:
#            return self.extensions_map[ext]
#        ext = ext.lower()
#        if ext in self.extensions_map:
#            return self.extensions_map[ext]
#        else:
#            return self.extensions_map['']
#
#    if not mimetypes.inited:
#        mimetypes.init() # try to read system mime.types
#    extensions_map = mimetypes.types_map.copy()
#    extensions_map.update({
#        '': 'application/octet-stream', # Default
#        '.py': 'text/plain',
#        '.c': 'text/plain',
#        '.h': 'text/plain',
#        })

