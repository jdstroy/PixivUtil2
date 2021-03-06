# -*- coding: UTF-8 -*-
import PixivUtil2
import PixivBrowserFactory
import PixivConfig
import getpass

__config__    = PixivConfig.PixivConfig()
__config__.loadConfig()
__br__ = PixivUtil2.__br__ = PixivBrowserFactory.getBrowser(config=__config__)

def prepare():
    ## Log in
    username = __config__.username
    if username == '':
        username = raw_input('Username ? ')
    password = __config__.password
    if password == '':
        password = getpass.getpass('Password ? ')

    result = False
    if len(__config__.cookie) > 0:
        result = PixivUtil2.pixiv_login_cookie()

    if not result:
        if __config__.useSSL:
            result = PixivUtil2.pixiv_login_ssl(username,password)
        else:
            result = PixivUtil2.pixiv_login(username,password)

    return result

def downloadPage(url, filename):
    print "Dumping " + url + " to " + filename
    html = __br__.open(url).read()
    try:
        dump = file(filename, 'wb')
        dump.write(html)
        dump.close()
    except :
        pass

def main():
    result = prepare()
    if result:
        ## ./test/test-image-manga.htm
        ## http://www.pixiv.net/member_illust.php?mode=medium&illust_id=28820443
        downloadPage('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=28820443', './test/test-image-manga.htm')

        ## ./test/test-image-unicode.htm
        ## http://www.pixiv.net/member_illust.php?mode=medium&illust_id=2493913
        downloadPage('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=2493913', './test/test-image-unicode.htm')

        ## ./test/test-helper-avatar-name.htm
        ## http://www.pixiv.net/member_illust.php?id=1107124
        downloadPage('http://www.pixiv.net/member_illust.php?id=1107124', './test/test-helper-avatar-name.htm')

        downloadPage('http://www.pixiv.net/member_illust.php?id=1', './test/test-nouser.htm')
        downloadPage('http://www.pixiv.net/member_illust.php?id=26357', './test/test-member-noavatar.htm')
        downloadPage('http://www.pixiv.net/member_illust.php?id=1233', './test/test-noimage.htm')
        downloadPage('http://www.pixiv.net/bookmark.php?id=3281699', './test/test-member-bookmark.htm')

        downloadPage('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=32039274', './test/test-image-info.html')
        downloadPage('http://www.pixiv.net/bookmark_new_illust.php', './test/test-bookmarks_new_ilust.htm')
        downloadPage('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=12467674', './test/test-image-my_pick.html')
        downloadPage('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=20496355', './test/test-image-noavatar.htm')
        downloadPage('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=11164869', './test/test-image-parse-tags.htm')
        downloadPage('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=9175987', './test/test-image-no_tags.htm')
        downloadPage('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=28865189', './test/test-image-rate_count.htm')
        ## downloadPage('http://www.pixiv.net/member_illust.php?mode=big&illust_id=20644633', './test/test-image-parsebig.htm')
        downloadPage('http://www.pixiv.net/member_illust.php?mode=manga&illust_id=20592252', './test/test-image-parsemanga.htm')
        downloadPage('http://www.pixiv.net/bookmark.php', './test/test-image-bookmark.htm')

        downloadPage('http://www.pixiv.net/member_illust.php?id=313631&p=4', './test/test-tags-member-search-last.htm')
        downloadPage('http://www.pixiv.net/search.php?word=%E5%88%9D%E6%98%A5%E9%A3%BE%E5%88%A9&s_mode=s_tag_full', './test/test-tags-search-exact.htm')
        downloadPage('http://www.pixiv.net/search.php?word=%E3%81%93%E3%81%AE%E4%B8%AD%E3%81%AB1%E4%BA%BA%E3%80%81%E5%A6%B9%E3%81%8C%E3%81%84%E3%82%8B!&s_mode=s_tag_full&order=date_d&p=12', './test/test-tags-search-partial.htm')
        downloadPage('http://www.pixiv.net/search.php?s_mode=s_tag_full&word=XXXXXX','./test/test-tags-search-exact-parse_details.htm')
        downloadPage('http://www.pixiv.net/search.php?s_mode=s_tag&word=%E3%81%93%E3%81%AE%E4%B8%AD%E3%81%AB1%E4%BA%BA%E3%80%81%E5%A6%B9%E3%81%8C%E3%81%84%E3%82%8B!','./test/test-tags-search-partial.htm')
        downloadPage('http://www.pixiv.net/search.php?word=%E3%81%93%E3%81%AE%E4%B8%AD%E3%81%AB1%E4%BA%BA%E3%80%81%E5%A6%B9%E3%81%8C%E3%81%84%E3%82%8B!&order=date_d&p=12','./test/test-tags-search-partial-last.htm')

        downloadPage('http://www.pixiv.net/search.php?s_mode=s_tag&word=R-18%20K-On!','./test/test-tags-search-skip-showcase.htm')
        ## Not updated:
        ## ./test/test-login-error.htm
        ## ./test/test-member-suspended.htm
        ## ./test/test-member-nologin.htm

if __name__ == '__main__':
    main()
