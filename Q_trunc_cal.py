def Q_trunc_cal(dpi,wavelength,ftheta,m):
    x=np.pi*dpi/wavelength
    S11 = [ps.MatrixElements(m,wavelength,dpi,np.cos(thetai*np.pi/180))[0] for thetai in ftheta.index]
    Q_trunc = np.pi/180*.25*np.sum(S11*ftheta.ftheta*2)/((np.pi*dpi/wavelength)**2)
    return Q_trunc
