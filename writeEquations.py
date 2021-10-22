try:
    from StringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

import matplotlib.pyplot as plt
try:
    import AM_Equations as am
except:
    None
try:
    import JF_Equations as jf
except:
    None
try:
    import MR_Equations as mr
except:
    None

def render_latex(formula, fontsize=12, dpi=300, format_='svg'):
    """Renders LaTeX formula into image."""
    fig = plt.figure()
    text = fig.text(0, 0, u'{0}'.format(formula), fontsize=fontsize)

    fig.savefig(BytesIO(), dpi=dpi)  # triggers rendering

    bbox = text.get_window_extent()
    width, height = bbox.size / float(dpi) + 0.05
    fig.set_size_inches((width, height))

    dy = (bbox.ymin / float(dpi)) / height
    text.set_position((0, -dy))

    buffer_ = BytesIO()
    fig.savefig(buffer_, dpi=dpi, transparent=True, format=format_)
    plt.close(fig)
    buffer_.seek(0)

    return buffer_.getvalue()


if __name__ == '__main__':

    d1 = am.Data()
    #d2 = jf.Data()
    #d3 = mr.Data()

    

    ########## AM ##########

    for num in range(len(d1.equations)):

        img = 'img'+str(num)+'.png'

        image_bytes = render_latex(d1.equations[num], format_='png')

        with open(img, 'wb') as image_file:
            image_file.write(image_bytes)

    ########################




    ########## JF ##########

    """for num in range(len(d2.equations)):

        img = 'img'+str(num+1)+'.png'

        image_bytes = render_latex(d2.equations[num+1], format_='png')

        with open(img, 'wb') as image_file:
            image_file.write(image_bytes)"""

    ########################








    ########## MR ##########

    """for num in range(len(d3.equations)):

        img = 'img'+str(num)+'.png'

        image_bytes = render_latex(d3.equations[num], format_='png')

        with open(img, 'wb') as image_file:
            image_file.write(image_bytes)"""

    ########################